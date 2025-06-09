# Create your views here.

from django.shortcuts import render
from .forms import PuzzleForm
import random

def puzzle_view(request):
    result = None

    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Number Puzzle
            if number % 2 == 0:
                number_result = f"The number {number} is even. Its square root is {number**0.5:.2f}."
            else:
                number_result = f"The number {number} is odd. Its cube is {number ** 3}."

            # Text Puzzle
            binary_message = ' '.join(format(ord(char), '08b') for char in message)
            vowels = 'aeiouAEIOU'
            vowel_count = sum(1 for char in message if char in vowels)

            # Treasure Hunt
            target = random.randint(1, 100)
            attempts = []
            for i in range(5):
                guess = random.randint(1, 100)
                if guess < target:
                    feedback = "Too low!"
                elif guess > target:
                    feedback = "Too high!"
                else:
                    feedback = "Correct!"
                
                attempts.append({
                    'attempt': i+1,
                    'guess': guess,
                    'feedback': feedback
                })
                
                if guess == target:
                    break
            
            if attempts[-1]['feedback'] == "Correct!":
                treasure_result = f"Treasure found in {len(attempts)} attempts!"
            else:
                treasure_result = f"Failed to find treasure in 5 attempts. The secret number was {target}."

            result = {
                'number_result': number_result,
                'binary_message': binary_message,
                'vowel_count': vowel_count,
                'secret_number': target,
                'attempts': attempts,
                'treasure_summary': treasure_result,
            }
        # If the input value is invalid
        else:
            result = None
            
    # If the HTTP Request method is not "POST"
    else:
        form = PuzzleForm()

    return render(request, 'puzzle/form.html', {'form': form, 'result': result})


