import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Answer} from "../models/answer";

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class AnswerService {
  baseUrl:string = 'http://127.0.0.1:8000/api/answers/'
  constructor(private http:HttpClient) { }

  // Get Answers
  getAnswers():Observable<Answer[]>{
    return this.http.get<Answer[]>(this.baseUrl);
  }

  // Delete Answer
  deleteAnswer(answer:Answer):Observable<Answer> {
    const url = `${this.baseUrl}${answer.id}`;
    return this.http.delete<Answer>(url, httpOptions);
  }

  // Add Answer
  addAnswer(answer:Answer):Observable<Answer> {
    return this.http.post<Answer>(this.baseUrl, answer, httpOptions);
  }

}
