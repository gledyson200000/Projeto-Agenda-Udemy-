from django.shortcuts import render, redirect
from django.contrib import auth, messages
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, f'{user.username} logado com sucesso!')
            return redirect('contact:index')
        messages.error(request, 'Login invalido! Tente Novamente')

    return render(
        request, 
        'contact/login.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login_view')

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
         return render(
            request, 
            'contact/user_update.html',
            {
                'form': form
            }
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request, 
            'contact/user_update.html',
            {
                'form': form
            }
        )
    
    form.save()
    messages.success(request, 'Usuario atualizado com sucesso!')
    return redirect('contact:user_update')