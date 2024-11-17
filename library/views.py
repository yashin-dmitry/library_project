from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Book


class BooksListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/books_detail.html'
    context_object_name = 'book'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')

# def books_list(requests):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render(request, 'library/books_list.html', context)
#
# def books_detail(requests, book_id):
#     book = Book.objects.get(id=book_id):
#     context = {'book': book}
#     return render(request, 'library/books_list.html', context)
