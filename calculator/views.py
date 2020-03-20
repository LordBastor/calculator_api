from cexprtk import evaluate_expression, ParseException

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EvaluateExpression(APIView):
    """
    View allowing users to evaluate a mathematical expression

    * Does not require authentication and is open to the public.
    """

    def post(self, request):
        """
        Evaluates if an expression is valid and either returns a validation error
        or the evaluation of the given expression
        """
        data = request.data

        if "expression" in data and data["expression"]:
            expression = data["expression"]

            try:
                result = evaluate_expression(expression, {})
            except (SyntaxError, ParseException):
                return Response(
                    data={
                        "validation_error": (
                            "Please check the validity of the"
                            " mathematical expression and try again"
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(data={"result": result}, status=status.HTTP_200_OK)

        return Response(
            data={"validation_error": "expression can not be blank or missing"}
        )
