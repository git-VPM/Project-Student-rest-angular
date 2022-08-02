import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Dist, Student } from '../models/student.model';

const baseUrl = 'http://127.0.0.1:8000';

@Injectable({
  providedIn: 'root'
})
export class StudentService {
  constructor(private http: HttpClient) { }
  getAll(): Observable<Student[]> {
    return this.http.get<Student[]>(baseUrl);
  }
  get(id: any): Observable<Student> {
    return this.http.get(`${baseUrl}/${id}`);
  }
  post(data: any): Observable<any> {
    return this.http.post(baseUrl, data);
  }
  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }
  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }
  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }
  findByName(name: any): Observable<Student[]> {
    return this.http.get<Student[]>(`${baseUrl}?name=${name}`);
  }
  // getlist(): Observable<any> {
  //   return this.http.get<any>(baseUrl + '/students')

  getdist(): Observable<Dist[]> {
    return this.http.get<Dist[]>(baseUrl + '/dist'); //connect backend to get dist data
  }
  getid(id: any): Observable<any> {
    return this.http.get(`${baseUrl + '/dist'}/${id}`); //connect backend to get dist by pk_bint_id
  }
}