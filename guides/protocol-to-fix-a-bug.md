# How to fix a bug

Fixing a bug seems like an easy or obvious task. Nonetheless, this process actually hides several dimensions that are
worth mentioning explicitly. In order to properly fix a bug, let's define success first. What are the expected properties of 
this process?

1. The bug has to be worth fixing
2. The bug should be fixed at the root cause 
3. The bug should be solved only once

## 1. The bug has to be worth fixing

Whenever you have a bug, first triage it ([source](https://blog.codinghorror.com/not-all-bugs-are-worth-fixing/)):
- Severity: When this bug happens, how bad is the impact?
- Frequency: How often does this bug happen?
- Cost: How much effort would be required to fix this bug?
- Risk: What is the risk of fixing this bug?

If your evaluation concludes that this bug is worth solving, proceed to the next section.

## 2. The bug should be fixed at the root cause

When your boss asks you, "Did you fix the bug?", you should be confident when replying, **yes I did**.
In order to show confidence, you need to first prove to yourself that you solved it. In other words,
to prove causality. These are the steps I follow to prove causality:

- Reproduce the bug: make sure you are able to reproduce the bug locally 
- Find the root cause(s) of the bug: sometimes a bug is created in step 5, flows through the program to step 19, and becomes visible at step 20. Make sure 
   you fix the bug at step 5, its real origin. Once you find the root cause, proceed to the next section.

## 3. The bug should be solved only once

Once you find the root cause, create an automatic test with the AAA pattern:
```python
def test__module__conditions__expected_output():
# Arrange
# set up here the initial conditions that generate the bug

# Act
# trigger the functions that create the bug

# Assert
# assert that the bug is not present
```

This test now **must fail** because the code fix is not yet in place. Two things could happen now:
- The test passes: this means the bug is not reproducible from this test, or it is reproducible but your assertions do not actually detect it. You need to 
  fix this test.
- The test fails: now you have reproduced the bug, and the assertions are not met because the code fix is not implemented yet.

Now you implement the code fix. Then the test should pass. Push a PR with this fix, explaining what happened. 
By creating an automatic test, you have effectively documented your knowledge of this bug into the codebase 
permanently. If in the future any developer attempts to make a code change that makes this test fail, it will be a reminder
that they can't do that because this bug could reappear.

