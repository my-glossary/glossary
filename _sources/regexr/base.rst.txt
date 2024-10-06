========
Основное
========

``/`` - Разделитель, его указывают в начале и конце регулярного
выражения, чтобы отделить регулярное выражение от остального текста.

=================
Playwright regexp
=================

`re.compile <https://docs.python.org/3/library/re.html#re.compile>`_

`IGNORECASE <https://docs.python.org/3/library/re.html#re.IGNORECASE>`_ - флаг

::

    expect(page.get_by_text(re.compile("welcome, john", re.IGNORECASE))).to_be_visible()