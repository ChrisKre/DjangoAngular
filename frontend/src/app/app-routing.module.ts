import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AnswersComponent} from "./components/answer/answers/answers.component";
import {RegistersComponent} from "./components/register/registers/registers.component";

const routes: Routes = [
  { path: 'register', component: RegistersComponent },
  { path: 'answer', component: AnswersComponent },


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
