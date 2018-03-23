test = {
  'name': 'Question 1_',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert type(q5_integral_10_samples) == float # result is not a float
          >>> assert type(q5_integral_100_samples) == float # result is not a float
          >>> assert type(q5_integral_1000_samples) == float # result is not a float
          >>> assert type(q5_integral_quad) == float # result is not a float
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
