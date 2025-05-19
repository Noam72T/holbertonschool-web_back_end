const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');

    const headers = lines[0].split(',').map(h => h.trim());
    const fieldIndex = headers.indexOf('field');
    const firstNameIndex = headers.indexOf('firstname');

    if (fieldIndex === -1 || firstNameIndex === -1) {
      throw new Error('Cannot parse header columns');
    }

    const studentsByField = {};

    for (let i = 1; i < lines.length; i++) {
      const parts = lines[i].split(',').map(p => p.trim());
      if (parts.length === headers.length) {
        const field = parts[fieldIndex];
        const firstName = parts[firstNameIndex];

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);
      }
    }

    const totalStudents = Object.values(studentsByField).reduce((a, b) => a + b.length, 0);

    console.log(`Number of students: ${totalStudents}`);
    for (const [field, names] of Object.entries(studentsByField)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
