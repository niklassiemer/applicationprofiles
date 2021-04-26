import os.path
import unittest
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList, MetaDataSchemes
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataField as Field


class TestFieldList(unittest.TestCase):
    def setUp(self):
        self.list = FieldList()

    def test_append(self):
        self.list.append(Field('foo'))
        self.assertRaises(TypeError, self.list.append, 'bar')
        self.assertRaises(TypeError, self.list.append, FieldList())

    def test_add(self):
        self.list.add('foo')
        self.list.add('bar', name='bar_name')
        self.assertRaises(TypeError, self.list.add, 'baz', not_a_kwarg=42)
        self.assertRaises(TypeError, self.list.add)

    def test___init__(self):
        list_of_fields = [Field('foo'), Field('bar')]
        field_list = FieldList(list_of_fields)
        self.assertEqual(field_list[0].name, 'foo')
        self.assertEqual(field_list[-1].name, 'bar')
        self.assertEqual(len(field_list), 2)
        list_of_fields.append('NotAField')
        self.assertEqual(len(field_list), 2)
        self.assertRaises(TypeError, FieldList, list_of_fields)

    def test___getitem__(self):
        self.list.add('foo')
        self.list.add('bar')
        self.assertEqual(self.list[0].name, 'foo')
        self.assertEqual(self.list[-1].name, 'bar')
        self.assertEqual(self.list[:1][0].name, 'foo')

    def test___next__(self):
        self.list.add('foo')
        self.list.add('bar')
        for field, target_name in zip(self.list, ['foo', 'bar']):
            self.assertEqual(field.name, target_name)

    def test___add__(self):
        self.list.add('foo')
        other = FieldList()
        other.add('bar')
        added = self.list + other
        self.assertListEqual([field.name for field in added], ['foo', 'bar'])
        self.assertRaises(TypeError, self.list.__add__, 'not_a_field_list')
        self.assertTrue(type(added._fields) == list)

    def test___iadd__(self):
        self.list.add('foo')
        other = FieldList()
        other.add('bar')
        self.list += other
        self.assertListEqual([field.name for field in self.list], ['foo', 'bar'])
        self.assertRaises(TypeError, self.list.__iadd__, 'not_a_field_list')
        self.assertTrue(type(self.list._fields) == list)

    def test___len__(self):
        self.assertEqual(len(self.list), 0)
        self.list.add('foo')
        self.assertEqual(len(self.list), 1)

    def test_copy(self):
        self.list.add('foo')
        self.list.add('bar')
        new_list = self.list.copy()
        self.assertListEqual(
            [field.name for field in self.list],
            [field.name for field in new_list]
        )
        new_list[0].field_type = 'boolean'
        self.assertFalse('boolean' == self.list[0].field_type)
        new_list.add('baz')
        self.assertEqual(len(self.list), 2)
        self.assertEqual(len(new_list), 3)

    def test_sort_fields_by_order_parameter(self):
        self.list.add('foo')
        self.list.add('bar')
        self.list.add('foo1', order_priority=1)
        self.list.add('foo2', order_priority=2)
        self.list.add('foo-1', order_priority=-1)
        self.list.add('foo-2', order_priority=-2)
        self.assertEqual([field.order_priority for field in self.list], [None, None, 1, 2, -1, -2])
        self.list.sort_fields_by_order_priority()
        self.assertEqual([field.order_priority for field in self.list], [1, 2, None, None, -2, -1])


class TestMetaDataScheme(unittest.TestCase):
    def setUp(self):
        self.list = FieldList()
        self.list.add('foo')
        self.list.add('bar')
        self.scheme = MetaDataSchemes('MyScheme')
        self.scheme.fields = self.list

    def test___init__(self):
        self.assertTrue(type(self.scheme.fields) == FieldList)

    def test_sort_fields_by_order_parameter(self):
        self.scheme.fields._fields.sort()

    def test_write(self):
        with open('tests/static_test_MyScheme_ttl') as f:
            compare_lines = f.readlines()

        self.assertFalse(os.path.isfile('MyScheme.ttl'))
        self.scheme.write()
        with open('MyScheme.ttl') as f:
            lines = f.readlines()
        self.assertEqual(lines, compare_lines)
        os.remove('MyScheme.ttl')

        self.assertFalse(os.path.isfile('testWriteMyScheme.ttl'))
        self.scheme.write('testWriteMyScheme')
        with open('testWriteMyScheme.ttl') as f:
            lines = f.readlines()
        self.assertEqual(lines, compare_lines)
        os.remove('testWriteMyScheme.ttl')

        self.assertFalse(os.path.isfile('MyScheme.txt'))
        self.scheme.write(file_extension='.txt')
        with open('MyScheme.txt') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0].split(), ['foo', ':', '(string)'])
        self.assertEqual(lines[1].split(), ['bar', ':', '(string)'])
        os.remove('MyScheme.txt')

        self.assertFalse(os.path.isfile('MyScheme.txt'))
        self.scheme.write(filename='MyScheme.txt')
        with open('MyScheme.txt') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0].split(), ['foo', ':', '(string)'])
        self.assertEqual(lines[1].split(), ['bar', ':', '(string)'])
        os.remove('MyScheme.txt')

        with self.assertRaises(ValueError):
            self.scheme.write(filename='some.txt', file_extension='.ttl')

        with self.assertRaises(ValueError):
            self.scheme.write(filename='some_file_without_valid.extension')
