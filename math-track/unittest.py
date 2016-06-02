def test(expected, actual, floatComparison=False):                                                                                                   
   if ((floatComparison and abs(expected - actual) > 1e-10) or
         (not floatComparison and expected != actual)):
      import sys, traceback
      (filename, lineno, container, code) = traceback.extract_stack()[-2]
      print("Test: %r failed on line %d in file %r.\nExpected %r but got %r\n" %
         (code, lineno, filename, expected, actual))

      sys.exit(1)
