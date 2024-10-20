====
Ruff
====

.. code-block::

    # Configuring Ruff
    # https://docs.astral.sh/ruff/configuration/

    exclude = [
        ".github/*",
        ".idea/*",
        ".venv/*",
        "docker/*",
        "postgres_data/*",
        "templates/*",
        ".env*",
        "*/migrations/*",
    ]
    line-length = 79

    [lint]
    preview = true  # checks will include unstable rules and fixes
    select = [
        "F",    # pyflakes: https://pypi.org/project/pyflakes/
        "E",    # pycodestyle: Error; pycodestyle: https://pypi.org/project/pycodestyle/
        "W",    # pycodestyle: Warning
        "I",    # isort: https://pypi.org/project/isort/
        "N",    # pep8-naming: https://pypi.org/project/pep8-naming/
        "D",    # pydocstyle: https://pypi.org/project/pydocstyle/
        "B",    # flake8-bugbear: https://pypi.org/project/flake8-bugbear/
        "C90",  # mccabe: https://pypi.org/project/mccabe/
    #    "UP",   # pyupgrade: https://pypi.org/project/pyupgrade/
    #    "YTT",  # flake8-2020: https://pypi.org/project/flake8-2020/
        "ANN",  # flake8-annotations: https://pypi.org/project/flake8-annotations/
    #    "S",    # flake8-bandit: https://pypi.org/project/flake8-bandit/
    #    "BLE",  # flake8-blind-except: https://pypi.org/project/flake8-blind-except/
    #    "FBT",  # flake8-boolean-trap: https://pypi.org/project/flake8-boolean-trap/
    #    "A",    # flake8-builtins
    #    "COM",  # flake8-commas
    #    "CPY",  # flake8-copyright
    #    "C4",   # flake8-comprehensions
    #    "DTZ",  # flake8-datetimez
    #    "T10",  # flake8-debugger
    #    "DJ",   # flake8-django
    #    "EM",   # flake8-errmsg
    #    "EXE",  # flake8-executable
    #    "FA",   # flake8-future-annotations
    #    "ISC",
    #    "ICN",
    #    "LOG",
    #    "G",
    #    "INP",
    #    "PIE",
    #    "T20",
    #    "PYI",
    #    "PT",   # flake8-pytest-style
        "Q",    # flake8-quotes: https://pypi.org/project/flake8-quotes/
    #    "RSE",  # flake8-raise
    #    "RET",  # flake8-return
    #    "SLF",  # flake8-self
    #    "SLOT",
    #    "SIM",
    #    "TID",
    #    "TCH",  # flake8-type-checking
    #    "INT",  # flake8-gettext
    #    "ARG",  # flake8-unused-arguments
    #    "PTH",  # flake8-use-pathlib
        "TD",   # flake8-todos: https://github.com/orsinium-labs/flake8-todos/
    #    "FIX",
    #    "ERA",
    #    "PD",
    #    "PGH",
    #    "PL",
    #    "TRY",
    #    "FLY",
    #    "NPY",
    #    #"FAST", # FastAPI
    #    "AIR",  # AIR
    #    "PERF", # PERF
    #    "FURB",
    #    #"DOC",  # pydoclint
    #    "RUF",  # Ruff-specific rules
    ]
    ignore = [
        'D203',     # 1 blank line required before class docstring
        'D211',     # No blank lines allowed before class docstring
        'D213',     # Multi-line docstring summary should start at the second line
        'D416',     # Section name should end with a colon
    ]

    [lint.flake8-quotes]
    inline-quotes = "single"

    [format]
    quote-style = "single"

    [lint.pycodestyle]
    max-doc-length = 72
