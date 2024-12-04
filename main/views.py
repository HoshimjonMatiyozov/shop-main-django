from django.shortcuts import redirect, render
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,DetailView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Shop, Product
from .forms import ShopForm, ProductForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
# from .permissions import CanAddShopPermission, CanAddProductPermission

class MainIndex(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:shop_create')  
            else:
                messages.error(request, "Noto'g'ri username yoki parol")
        
        return self.render_to_response({'form': form})


class ShopCreateView( LoginRequiredMixin , PermissionRequiredMixin, CreateView):
    model = Shop
    form_class = ShopForm
    template_name = 'main/shop_form.html'
    success_url = reverse_lazy('main:product_create')  
    permission_required = 'main.add_shop'  
    
    def form_valid(self, form):
        
        # Tizimga kirgan foydalanuvchini shop'ga bog'lash
        form.instance.user = self.request.user
        form.instance.status = 0  # Yangi shop - tasdiqlanmagan
        messages.success(self.request, "Magazin qo'shildi. Admin tasdiqlashi kerak.")
        return super().form_valid(form)

class ProductDetailView(DetailView):
    model = Product  # Product modelini ishlatamiz
    template_name = 'main/product_detail.html'  # HTML template
    context_object_name = 'product'  # template'da ishlatadigan o'zgaruvchi nomi
    
    def get_object(self, queryset=None):
        return self.model.objects.get(name_uz=self.kwargs['name'])  # URL'dan mahsulot nomini olib, bazadan qidiramiz
    

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    permission_required = 'main.add_product'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.status = 0  # Yangi mahsulot
        messages.success(self.request, "Mahsulot qo'shildi. Admin tasdiqlashi kerak.")
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('main:product_detail', kwargs={'name_uz': self.object.name_uz})