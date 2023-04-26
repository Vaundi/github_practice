def decimal_to_hexadecimal(decimal_number):
  """
  Converts a decimal number to hexadecimal.

  Args:
    decimal_number: The decimal number to convert.

  Returns:
    The hexadecimal number.
  """

  hexadecimal_number = ""
  while decimal_number > 0:
    remainder = decimal_number % 16
    hexadecimal_number = str(remainder) + hexadecimal_number
    decimal_number //= 16

  return "0x" + hexadecimal_number
