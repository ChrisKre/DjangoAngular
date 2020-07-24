import {Component, EventEmitter, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-add-answer',
  templateUrl: './add-answer.component.html',
  styleUrls: ['./add-answer.component.css']
})
export class AddAnswerComponent implements OnInit {

  @Output() addAnswer: EventEmitter<any> = new EventEmitter();
  text: string;

  constructor() { }

  ngOnInit(): void {
  }

  onSubmit() {
    const answer = {
      text: this.text,
    }
    this.addAnswer.emit(answer);
  }
}
