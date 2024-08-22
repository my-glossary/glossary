###############
Django Examples
###############

Get data from request
=====================

.. code-block:: python

   from json import loads
   def login(request):
       json = loads(request.body)
       print(json['username']) # Prints the value associated with

Send data from httpx library to DRF
===================================

   params from GET or POST

.. code-block:: python
   :caption: httpx:

   with httpx.Client() as client:
       response = client.post(
           'http://127.0.0.1:8000/api/v1/math-calc-exercise',
           data={'task_type': 'mul'},
       )

.. code-block:: python
   :caption: DRF view:

   class MathCalculateExerciseAPIView(APIView):
       """Mathematical calculate exercise view."""

       def post(self, request: Request) -> Response:
           """Render the task question."""
           task_type = request.POST.get('task_type')
           task_data = TaskFactory.create_task(task_type)
           return Response(task_data)

.. code-block:: python
   :caption: GET vs POST requests

   with httpx.Client() as client:
      response = client.post(
          'http://127.0.0.1:8000/api/v1/math-calc-exercise/',
          params={
              'task_type': 'mul',
              'min_value': 1,
              'max_value': 9,
          },
          data={
              'data': 'mul',
              'min_value': 1,
              'max_value': 9,
          },
      )

   request.GET = <QueryDict: {'task_type': ['mul'], 'min_value': ['1'], 'max_value': ['9']}>
   request.query_params = <QueryDict: {'task_type': ['mul'], 'min_value': ['1'], 'max_value': ['9']}>

   request.POST = <QueryDict: {'data': ['mul'], 'min_value': ['1'], 'max_value': ['9']}>
   request.query_params = <QueryDict: {'task_type': ['mul'], 'min_value': ['1'], 'max_value': ['9']}>
   request.data = <QueryDict: {'data': ['mul'], 'min_value': ['1'], 'max_value': ['9']}>

DRF simple Response
===================

.. code-block:: python

   class WordListAPIView(APIView):
       """English-Russian word list views."""

       def get(self, request: Request) -> Response:
           """Render English-Russian word list."""
           return Response(
               [
                   {'eng_word': 'black', 'rus_word': 'черный'},
                   {'eng_word': 'red', 'rus_word': 'красный'},
                   {'eng_word': 'blue', 'rus_word': 'синий'},
               ]
           )

.. code-block:: python
   :caption: Use words.values()

   class WordListAPIView(APIView):
       """English-Russian word list views."""

       def get(self, request: Request) -> Response:
           """Render English-Russian word list."""
           words = Word.objects.all()
           return Response(words.values())
