from django.shortcuts import render, get_object_or_404


from django.http import HttpResponseRedirect

from .models import MainMenu, Book, Order, OrderItem

from .forms import BookForm, ReviewForm

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required





# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def index(request):
    # return HttpResponse("<h1 align='center'>Helloooo World</h1> <h2>This is a try</h2>")
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
            'bookMng/home.html',
            {
              'item_list': MainMenu.objects.all()
            }
            )


@login_required(login_url=reverse_lazy('login'))
def cart(request):
    user = request.user

    # create object or query existing object
    order, created = Order.objects.get_or_create(user=user, complete=False)
    # it will get all the orderitems that have order as the parent 
    items = order.orderitem_set.all()

    return render(request, 'bookMng/cart.html', 
    {
        'item_list': MainMenu.objects.all(),
        'items': items,
        'order': order
    }
    )

@login_required(login_url=reverse_lazy('login'))
def checkout(request):
    return render(request, 'bookMng/checkout.html',
    {

    }
    )

@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
        b.picture = str(b.picture)[6:]
    return render(request,
            'bookMng/displaybooks.html',
            {
                'item_list': MainMenu.objects.all(),
                'books': books
            })

@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
            'bookMng/postbook.html',
            {
              'form': form,
              'item_list': MainMenu.objects.all(),
              'submitted': submitted
            }
            )




@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    picture = str(book.picture)[6:]
    reviews = book.review_set.all()
    return render(request,
            'bookMng/book_detail.html',
            {
                'item_list': MainMenu.objects.all(),
                'book': book,
                'picture': picture,
                'reviews': reviews
            }
            )


@login_required(login_url=reverse_lazy('login'))
def postreview(request, book_id):
    submitted = False
    book = get_object_or_404(Book, pk=book_id)
    reviews = book.review_set.all()
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return HttpResponseRedirect('/displaybooks/book_detail/{}'.format(book_id))

    else:
        form = ReviewForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'bookMng/postreview.html',
            {
                'book': book,
                'form': form,
                'item_list': MainMenu.objects.all(),
                'submitted': submitted,
                'reviews': reviews,
            })



def searchbar(request):
     if request.method == 'GET':
         search = request.GET.get('search')
         book = Book.objects.get(name=search)
         picture = str(book.picture)[6:]
         reviews = book.review_set.all()
         return render(request,
                       'bookMng/book_detail.html',
                       {
                           'item_list': MainMenu.objects.all(),
                           'book': book,
                           'picture': picture,
                           'reviews': reviews
                       })



class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)