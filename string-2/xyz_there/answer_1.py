"""
Takes (str str) input, 
task: Return whether str contains the substring 'xyz' and is not preceeded by a period

Other answer:
  return str.startswith('xyz') or any((str[i] != '.' and str[i+1:i+4] == 'xyz') for i in range(len(str) - 3))

Fails:
  return str.startswith('xyz') or (str[str.index('xyz') - 1] != '.')
  return str[str.index('xyz') - 1] != '.' if(str.index('xyz')) else str.startswith('xyz')
  return True if(str.startswith('xyz')) else (str[str.index('xyz') - 1] != '.')

  These fail the 'abc.xyzxyz' case because they only account for the first encounter of 'xyz' found 
  using the index() method. Additionally, find(), rindex(), and rfind() also won't work for similar reasons
"""

def xyz_there(str):
  is_xyz = (str.startswith('xyz'))
  
  # There's no need to loop over the string if we found 'xyz' at start
  if(not is_xyz):
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
