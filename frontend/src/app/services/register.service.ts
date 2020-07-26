import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {Register} from "../models/register";

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  baseUrl:string = 'http://127.0.0.1:8000/api/registers/'
  constructor(private http:HttpClient) { }

  // Get Registers
  getRegisters():Observable<Register[]>{
    return this.http.get<Register[]>(this.baseUrl);
  }

  // Delete Register
  deleteRegister(register:Register):Observable<Register> {
    const url = `${this.baseUrl}${register.id}`;
    return this.http.delete<Register>(url, httpOptions);
  }

  // Add Register
  addRegister(register:Register):Observable<Register> {
    console.log(register)
    return this.http.post<Register>(this.baseUrl, register, httpOptions);
  }
}
