import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Answer} from "../../../models/answer";
import {AnswerService} from "../../../services/answer.service";

@Component({
  selector: 'app-answer-item',
  templateUrl: './answer-item.component.html',
  styleUrls: ['./answer-item.component.css']
})
export class AnswerItemComponent implements OnInit {
  @Input() answer: Answer;
  @Output() deleteAnswer: EventEmitter<Answer> = new EventEmitter();

  constructor(private answerService:AnswerService) { }

  ngOnInit(): void {
  }

  onDelete(answer){
    this.deleteAnswer.emit(answer);
  }

}
