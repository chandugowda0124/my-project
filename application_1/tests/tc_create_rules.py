def test_create_rule():
    rule = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule)
    assert isinstance(ast, ASTNode)
    print("Create Rule Test Passed")
