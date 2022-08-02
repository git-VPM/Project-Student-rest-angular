import { Component, OnInit } from '@angular/core';
import { Dist, Student } from 'src/app/models/student.model';
import { StudentService } from 'src/app/services/student.service';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent implements OnInit {

  students?: Student[];
  currentStudent: Student = {};
  currentIndex = -1;
  // name = '';

  currentDist: Dist = {};

  constructor(private studentService: StudentService) { }
  ngOnInit(): void {
    this.retrieveStudents();
  }
  retrieveStudents(): void {
    this.studentService.getAll()
      .subscribe(
        data => {
          this.students = data;
          console.log(data, 'retrieveStudents');
        },
        error => {
          console.log(error);
        });
  }
  refreshList(): void {
    this.retrieveStudents();
    this.currentStudent = {};
    this.currentIndex = -1;
  }
  setActiveStudent(student: Student, index: number): void {
    this.currentStudent = student;
    this.currentIndex = index;
    console.log(student, 'active')
    this.retrieve_by_id(student.fk_dist);

  }
  retrieve_by_id(id: any): void {
    this.studentService.getid(id)
      .subscribe(
        data => {
          this.currentDist = data;
          console.log(data, 'retrieve_by_id');
        },
        error => {
          console.log(error);
        });
  }
  removeAllStudents(): void {
    this.studentService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.refreshList();
        },
        error => {
          console.log(error);
        });
  }
  deleteStudent(): void {
    this.studentService.delete(this.currentStudent.id)
      .subscribe(
        response => {
          console.log(response, 'delete by id');
          this.refreshList();
        },
        error => {
          console.log(error);
        });
  }
  // searchName(): void {
  //   this.currentStudent = {};
  //   this.currentIndex = -1;
  //   this.studentService.findByName(this.name)
  //     .subscribe(
  //       data => {
  //         this.students = data;
  //         console.log(data);
  //       },
  //       error => {
  //         console.log(error);
  //       });
  // }
}
