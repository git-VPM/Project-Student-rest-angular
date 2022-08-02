import { Component, OnInit } from '@angular/core';
import { StudentService } from 'src/app/services/student.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Dist, Student } from 'src/app/models/student.model';


@Component({
  selector: 'app-student-details',
  templateUrl: './student-details.component.html',
  styleUrls: ['./student-details.component.css']
})
export class StudentDetailsComponent implements OnInit {
  currentStudent: Student = {
    name: '',
    reg: '',
    gender: '',
    dob: '',
    address: '',
    fk_dist: 0,
  };
  dist?: Dist[];
  message = '';
  constructor(
    private studentService: StudentService,
    private route: ActivatedRoute,
    private router: Router) { }
  ngOnInit(): void {
    this.message = '';
    this.retrieveDist();
    this.getStudent(this.route.snapshot.params.id);
  }
  retrieveDist(): void {
    this.studentService.getdist()
      .subscribe(
        data => {
          this.dist = data;
          console.log(data, 'dist');
        },
        error => {
          console.log(error);
        });
  }
  getStudent(id: string): void {
    this.studentService.get(id)
      .subscribe(
        data => {
          this.currentStudent = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }
  change() {
    console.log()
  }
  updateStudent(): void {
    this.message = '';
    console.log(this.currentStudent, ' this.currentStudent');

    this.studentService.update(this.currentStudent.id, this.currentStudent)
      .subscribe(
        response => {
          console.log(response);
          this.message = response.message ? response.message : 'This student was updated successfully!';
          this.router.navigate(['/students']);
        },
        error => {
          console.log(error);
        });
  }
  deleteStudent(): void {
    this.studentService.delete(this.currentStudent.id)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/students']);
        },
        error => {
          console.log(error);
        });
  }
}
