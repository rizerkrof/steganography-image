#!/usr/bin/env python3
#
def tests_function(function, testing_samples):
    errors = []
    for sample in testing_samples:
        name, args, target = sample
        output = function(**args)
        if output != target:
            print(name, ':')
            print(output)
            print(target)
            errors.append(name+' FAILED')

    return not errors, "\n/!\ Errors occured in "+function.__name__+":\n{}".format("\t-> "+"\n\t-> ".join(errors))
