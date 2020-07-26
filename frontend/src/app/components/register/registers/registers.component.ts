import { Component, OnInit } from '@angular/core';
import {Register} from "../../../models/register";
import {RegisterService} from "../../../services/register.service";
import {Answer} from "../../../models/answer";

@Component({
  selector: 'app-registers',
  templateUrl: './registers.component.html',
  styleUrls: ['./registers.component.css']
})
export class RegistersComponent implements OnInit {
  registers: Register[];

  constructor(private registerService: RegisterService) { }

  ngOnInit(): void {
    this.registerService.getRegisters().subscribe( registers =>{
      this.registers = registers;
    })
  }

  deleteRegister(register:Register){
    this.registers = this.registers.filter(r => r.id !== register.id);
    this.registerService.deleteRegister(register).subscribe();
  }

  addRegister(register:Register) {
    this.registerService.addRegister(register).subscribe(register => {
      this.registers.push(register);
    });
  }

}
