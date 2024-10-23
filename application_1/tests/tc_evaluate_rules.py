def test_evaluate_rule():
    rule = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule)
    user_data = {"age": 35, "department": "Sales"}
    result = evaluate_rule(ast, user_data)
    assert result is True

    user_data = {"age": 25, "department": "Marketing"}
    result = evaluate_rule(ast, user_data)
    assert result is False

    print("Evaluate Rule Test Passed")
