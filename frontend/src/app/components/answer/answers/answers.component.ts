import { Component, OnInit } from '@angular/core';
import {Answer} from "../../../models/answer";
import {AnswerService} from "../../../services/answer.service";

@Component({
  selector: 'app-answers',
  templateUrl: './answers.component.html',
  styleUrls: ['./answers.component.css']
})
export class AnswersComponent implements OnInit {
  answers: Answer[];

  constructor(private answerService:AnswerService) { }

  ngOnInit(): void {
    this.answerService.getAnswers().subscribe(answers =>{
      this.answers = answers;
    });
    console.log(this.answers)
  }

  deleteAnswer(answer:Answer){
    this.answers = this.answers.filter(a => a.id !== answer.id);
    console.log(answer)
    this.answerService.deleteAnswer(answer).subscribe();
  }

  addAnswer(answer:Answer) {
    this.answerService.addAnswer(answer).subscribe(answer => {
      this.answers.push(answer);
    });
  }
}
