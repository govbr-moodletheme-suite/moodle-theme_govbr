from behave import then, when
from django.test import Client


@when('I request the page "{path}"')
def request_page(context, path):
    if not hasattr(context, "client"):
        context.client = Client()
    context.response = context.client.get(path)


@then("the response status should be 200")
def response_status_should_be_200(context):
    assert context.response.status_code == 200


@then('the page should contain "{text}"')
def page_should_contain(context, text):
    content = context.response.content.decode("utf-8")
    assert text in content
