from django.shortcuts import render
from django.http import HttpResponse
from MySite.helpers import *


def index(request):
    return render(request, 'index.html')


def fibonaci(request):
    if request.method == 'POST':
        number = int(request.POST.get('fibonacci', None))
        fibonacci_nums = fibonacci_numbers(number)
        return render(request, 'index.html', locals())


def factorial(request):
    if request.method == 'POST':
        number = int(request.POST.get('factorial', None))
        fact = get_factorial(number)
    return render(request, 'index.html', locals())


def primes(request):
    if request.method == 'POST':
        number = int(request.POST.get("prime", None))
        primes = prime_nmbers(number)
    return render(request, 'index.html', locals())


def encode(request):
    if request.method == 'POST':
        string = request.POST.get("text_for_encode", None)
        encode_str = encode_rle(string)
    return render(request, 'index.html', locals())


def decode(request):
    if request.method == 'POST':
        encode_string = request.POST.get("encoded_text", None)
        string_text = decode_rle(encode_string)
    return render(request, 'index.html', locals())
