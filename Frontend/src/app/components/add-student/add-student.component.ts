import { Component, OnInit } from '@angular/core';
import { Student, Dist } from 'src/app/models/student.model';
import { StudentService } from 'src/app/services/student.service';

@Component({
  selector: 'app-add-student',
  templateUrl: './add-student.component.html',
  styleUrls: ['./add-student.component.css']
})
export class AddStudentComponent implements OnInit {
  student: Student = {
    name: '',
    reg: '',
    gender: '',
    dob: '',
    address: '',
    fk_dist: undefined,
  };
  dist?: Dist[];

  submitted = false;
  constructor(private studentService: StudentService) { }
  ngOnInit(): void {
    this.retrieveDist();
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
  saveStudent(): void {

    const data = {
      'name': this.student.name,
      'reg': this.student.reg,
      'gender': this.student.gender,
      'dob': this.student.dob,
      'address': this.student.address,
      'fk_dist': Number(this.student.fk_dist)
    };
    console.log(data)
    if (data.name == '') {
      alert('Name cannot be empty')
      return
    } if (data.reg == '') {
      alert('Registration cannot be empty')
      return
    } if (data.gender == '') {
      alert('Select gender')
      return
    } if (data.dob == '') {
      alert('Date of birth cannot be empty')
      return
    } if (data.address == '') {
      alert('Address cannot be empty')
      return
    } if (data.fk_dist == undefined) {
      alert('Select district')
      return
    }
    console.log(this.student, 'student')
    this.studentService.post(data)
      .subscribe(
        response => {
          console.log(response);
          if (response.status == 0) {
            this.submitted = false
            alert('Invalid Registration Number')
          }
          else {
            this.submitted = true
          }
        },
        error => {
          console.log(error);
        });
  }
  newStudent(): void {
    this.submitted = false;
    this.student = {
      name: '',
      reg: '',
      gender: '',
      dob: '',
      address: '',
      fk_dist: 0
    };
  }
}
