Below is the complete, rewritten documentation with the updated running scenario integrated.

---

# Faculty Management Application

## 1. Problem Statement

A faculty requires a system that manages students, courses, and grade assignments. The system must support CRUD operations for students and courses, search functions, grade assignment with date tracking, and multiple reports. A student is considered enrolled in a course once they have at least one grade in that course. The system must also compute the top three most popular courses and the top 20% highest-performing students.

---

## 2. Feature List

1. **Student Management**

   * Add, delete, modify students
   * List all students
   * Search students by ID or name

2. **Course Management**

   * Add, delete, modify courses
   * List all courses
   * Search courses by ID, name or proffesor

3. **Grade Assignment**

   * Assign a grade with date for a student–course pair
   * Manage grade records : delete, modify a grade

4. **Reports**

   * For any course:
     * Students with grades sorted alphabetically
     * Students with grades sorted by grade

   * Top 3 most popular courses
   * Top 20% students by average grade

5. **System Architecture**

   * Layered design (UI → Service → Domain → Repository)

---

## 3. Iteration Plan

### **Iteration 1 – Architecture & Domain Foundations**

Layered architecture is established early (UI, Controller, Domain, Repository).
Deliverables:

* Domain classes: `Student`, `Course`, `Grade`
* Validation rules
* Repository interfaces and in-memory implementations
* Controller layer structure for students, courses, grades
* Initial UI connected to controllers
* Verified data flow across layers

### **Iteration 2 – Core Features**

Deliverables:

* CRUD for students and courses
* Search features
* Grade assignment with date
* Course reports (alphabetical, by grade)

### **Iteration 3 – Reporting & Refinement**

Deliverables:

* Top 3 most popular courses
* Top 20% students
* Complete UI flow and final validation
* Final integration tests

---

## 4. Running Scenario

1. User launches the program.
2. User **adds** a student with ID `S01` and name `Ana Ionescu`.
3. User **adds** a course with ID `C01`, name *Algebra*, professor *Marinescu*.
4. User **assigns** a grade of `9` to student `S01` in course `C01` on `10/01/2025`.
5. User **modifies** the student’s name from *Ana Ionescu* to *Ana Popescu*.
6. User **deletes** all grades assigned to student `S01` for course `C01`.
7. User **removes students** who have no grades; student `S01` is removed.
8. User performs an **undo** operation; student `S01` and her grade reappear.

---

## 5. Plan of Implementation for each feature

### 5.1 Student Management – Tasks (Iteration1)

1. Define the `Student` domain entity with validation rules.
2. Create a repository dedicated to storing and managing students.
3. Implement CRUD operations in the repository (add, remove, update, retrieve).
4. Add search utilities (by ID, by name fragment).
5. Build the student controller that coordinates input validation and repository access.
6. Integrate student operations with the undo service so all changes are reversible.
7. Connect controller operations to the UI menu and input parsing.
8. Test all student workflows end-to-end (add, modify, list, search, delete, undo).

---

### 5.2 Course Management – Tasks (Iteration1)

1. Define the `Course` domain entity with validation for ID, name, and professor.
2. Implement the repository for storing courses in memory.
3. Provide CRUD operations and search capabilities in the repository.
4. Build the course controller that exposes course management operations.
5. Ensure course deletions also delegate removal of associated grade records.
6. Attach course operations to the undo service.
7. Integrate the course controller with the UI menu and commands.
8. Perform integration tests for the complete course workflow.

---

### 5.3 Grade Assignment – Tasks(Iteration 2)

1. Define the `Grade` domain entity including grade value rules and date validation.
2. Build a grade repository capable of storing, retrieving, and removing grade records.
3. Implement grade assignment functionality in the controller (validate student and course existence).
4. Decide and enforce the policy for storing multiple grades or unique grade entries per student–course pair.
5. Integrate grade operations with the undo service.
6. Update the UI to allow grade assignment and grade listing for debugging.
7. Ensure all grade operations interact cleanly with student and course removal workflows.
8. Test grade assignment, removal, and undo operations thoroughly.

---

### 5.4 Reporting – Tasks(Iteration3)

1. Implement service/controller functions for generating course-based reports (alphabetical and by grade).
2. Add computation logic for determining course popularity based on unique students with grades.
3. Implement average-grade calculation for each student.
4. Compute and extract the top 20% of students based on their average.
5. Ensure sorting routines are deterministic and stable.
6. Connect report functions to UI commands.
7. Validate error cases (e.g., reporting on a course with no grades).
8. Test all reporting features with varied datasets.