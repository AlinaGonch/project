from django.shortcuts import render


def gallary_page(requests):
    return render(requests, 'gallary.html', {})