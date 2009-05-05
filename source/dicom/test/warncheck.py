# warncheck.py
# 
import warnings
import unittest

def assertWarns(self, warn_startswith, function, *func_args, **func_kwargs):
    """
    Check that the function generates the expected warning
    with the arguments given.
    
    warn_startswith -- the first part of the warning string
    function -- the function to call (expected to issue a warning)
    func_args -- positional arguments to the function
    func_kwargs -- keyword arguments to the function
    
    Return the function return value.
    """
    all_warnings = []
    def new_warn_explicit(*warn_args):
        all_warnings.append(warn_args[0]) # save only the message here

    saved_warn_explicit = warnings.warn_explicit
    try:
        warnings.warn_explicit = new_warn_explicit
        result = function(*func_args, **func_kwargs)
    finally:
        warnings.warn_explicit = saved_warn_explicit

    self.assert_(len(all_warnings)==1, "Expected one warning; got %d" % len(all_warnings))
    self.assert_(all_warnings[0].startswith(warn_startswith), 
        "Expected warning message '%s...'; got '%s'" % (warn_startswith, all_warnings[0]))
    return result
    
def test_warning(the_warning):
    if the_warning:
        warnings.warn(the_warning)

class WarnTests(unittest.TestCase):
    def testWarn(self):
        """Test that assertWarns works as expected"""
        assertWarns(self, "Look", test_warning, "Look out")
if __name__ == "__main__":
    unittest.main()
    