# QuBu

QuBu is a simple database query builder for Python.


## Build status

<!--[![Build Status](https://travis-ci.org/ashep/qubu.svg?branch=master)](https://travis-ci.org/ashep/qubu)-->
<!--[![Coverage](https://codecov.io/gh/ashep/qubu/branch/master/graph/badge.svg)](https://codecov.io/gh/ashep/qubu)-->


## Features

Currently supported only some of MongoDB's main operators, such as:

* Logical query operators:
[$and](https://docs.mongodb.com/manual/reference/operator/query/and/), 
[$or](https://docs.mongodb.com/manual/reference/operator/query/or/),
[$nor](https://docs.mongodb.com/manual/reference/operator/query/nor/),
[$not](https://docs.mongodb.com/manual/reference/operator/query/not/)
* Comparison query operators: 
[$eq](https://docs.mongodb.com/manual/reference/operator/query/eq/),
[$gt](https://docs.mongodb.com/manual/reference/operator/query/gt/),
[$gte](https://docs.mongodb.com/manual/reference/operator/query/gte/),
[$in](https://docs.mongodb.com/manual/reference/operator/query/in/),
[$lt](https://docs.mongodb.com/manual/reference/operator/query/lt/),
[$lte](https://docs.mongodb.com/manual/reference/operator/query/lte/),
[$ne](https://docs.mongodb.com/manual/reference/operator/query/ne/),
[$nin](https://docs.mongodb.com/manual/reference/operator/query/nin/)
* Evaluation query operators:
[$text](https://docs.mongodb.com/manual/reference/operator/query/text/),
[$regex](https://docs.mongodb.com/manual/reference/operator/query/regex/)
* Geospatial query operators:
[$near](https://docs.mongodb.com/manual/reference/operator/query/near/),
[$nearSphere](https://docs.mongodb.com/manual/reference/operator/query/nearSphere/)


## Requirements

- [Python](https://python.org)>=3.6
- [DicMer](https://github.com/ashep/dicmer)


## Installation

```bash
pip install qubu
```

## Usage

Following Python code:

```python
from qubu import And, Or, Not, Eq, Ne, Gt

e = Or(
    And(
        Eq('foo', 'bar'), 
        Ne('bar', 'baz')
    ),
    Not(Gt('salary', 1500)),
    Eq('allowed', True),
)

e.compile()
```

will give following object:

```python
{'$or': [
    {'$and': [
        {'foo': {'$eq': 'bar'}},
        {'bar': {'$ne': 'baz'}}
    ]}, 
    {'salary': {'$not': {'$gt': 1500}}}, 
    {'allowed': {'$eq': True}}
]}
``` 


## Documentation

Work in progress.


## Testing

```bash
python setup.py test
```


## Contributing

If you want to contribute to a project and make it better, your help is very 
welcome. Contributing is also a great way to learn more about social coding on 
Github, new technologies and and their ecosystems and how to make constructive, 
helpful bug reports, feature requests and the noblest of all contributions: 
a good, clean pull request.

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called 
  `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into 
  your local repository.
- Create a new branch to work on. Branch from `develop` if it exists, else from 
  `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them.
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's interactive rebase. Create 
  a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's 
  `develop` branch if there is one, else go for `master`.
- If the maintainer requests further changes just push them to your branch. 
- Once the pull request is approved and merged you can pull the changes from 
  `upstream` to your local repo and delete your extra branch(es).

And last but not least: Always write your commit messages in the present tense. 
Your commit message should describe what the commit, when applied, does to the 
code – not what you did to the code.


## Roadmap

* Write documentation.
* SQL expressions support.


## Support

If you have any issues or enhancement proposals feel free to report them via 
project's [Issue Tracker](https://github.com/ashep/qubu/issues). 


## Authors

* [Oleksandr Shepetko](https://shepetko.com) -- initial work.


## Credits

None


## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) 
file for details.
