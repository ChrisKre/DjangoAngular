import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Register} from "../../../models/register";

@Component({
  selector: 'app-register-item',
  templateUrl: './register-item.component.html',
  styleUrls: ['./register-item.component.css']
})
export class RegisterItemComponent implements OnInit {
  @Input() register: Register;
  @Output() deleteRegister: EventEmitter<Register> = new EventEmitter();
  constructor() { }

  ngOnInit(): void {
  }

  onDelete(register){
    this.deleteRegister.emit(register);
  }

}
