import {Component, EventEmitter, OnInit, Output, ViewChild} from '@angular/core';
import {RegisterType} from "../../../models/register";
import {
  ITdDynamicElementConfig,
  TdDynamicElement,
  TdDynamicFormsComponent,
  TdDynamicType
} from "@covalent/dynamic-forms";

@Component({
  selector: 'app-add-register',
  templateUrl: './add-register.component.html',
  styleUrls: ['./add-register.component.css']
})
export class AddRegisterComponent implements OnInit {
   @Output() AddRegister: EventEmitter<any> = new EventEmitter();
   @ViewChild(TdDynamicFormsComponent) formValues: TdDynamicFormsComponent;

  registerForm: ITdDynamicElementConfig[] = [
   {
     name: 'name',
     hint: 'name for register',
     type: TdDynamicElement.Input,
     required: true,
     flex: 10,
   },
   {
     name: 'type',
     type: TdDynamicType.Array,
     selections: [RegisterType.LANGUAGE, RegisterType.KNOWLEDGE, RegisterType.SOFTWARE],
     default: RegisterType.LANGUAGE,
     flex: 10,
   },
 ];

  constructor() { }

  ngOnInit(): void {
  }

  onSubmit() {
    const register = {
      name: this.formValues.value.name,
      type: this.formValues.value.type,
    }
    console.log(register)
    this.AddRegister.emit(register);
  }
}
