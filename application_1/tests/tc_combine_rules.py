def test_combine_rules():
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "salary > 50000 OR experience > 5"
    combined_ast = combine_rules([rule1, rule2])
    assert combined_ast is not None
    print("Combine Rules Test Passed")
