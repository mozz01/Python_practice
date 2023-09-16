"""
Takes (str str) input, 
task: Return whether str contains the substring 'xyz' and is not preceeded by a period
"""
def xyz_there(str):
  is_xyz = (str.startswith('xyz'))

  for i in range(1, len(str) - 3):
    if((str[i+1:i+4]) == 'xyz' and str[i] != '.'):
      is_xyz = True

  return is_xyz


if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(xyz_there('abcxyz') == True)
  print(xyz_there('abc.xyz') == False)
  print(xyz_there('xyz.abc') == True)
  print(xyz_there('abc.xyzxyz') == True)
  print(xyz_there('1.xyz.xyz2.xyz') == False)
