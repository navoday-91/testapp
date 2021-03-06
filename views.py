from django.shortcuts import render
from .models import myapp
from django.template.context_processors import csrf
import itertools
import re
import string
# Create your views here.

def index(request):
    myappdata = myapp.objects.all()
    context = {
        'listdata': myappdata
    }
    return render(request, 'index.html', context )


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""

    # modify the code in this function.

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    firstletters = set(re.findall(r'\b([A-Z])[A-Z0-9]', formula))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z0-9]+)', formula))
    body = ''.join(tokens)
    if firstletters:
        tests = ' and '.join(L + '!=0' for L in firstletters)
        body = '%s and %s' % (tests, body)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print(f)
    return eval(f), letters


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words uncahanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10 ** i, d))
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def faster_solve(formula):
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            return "There was an Arithmetic Error! Please Retry."

def details(request, todo_id):
    todo = myapp.objects.get(id = todo_id)
    context = {
        'data': todo
    }
    return render(request, 'details.html', context)

def expression(request):
    if request.method == 'POST':
        expressionstring = request.POST['expression']
        solution = faster_solve(expressionstring)
        context = dict(expression=expressionstring, solution=solution)
        return render(request, 'expression.html', context)
    else:
        return render(request, 'expression.html')



