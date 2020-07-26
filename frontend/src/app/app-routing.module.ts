import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AnswersComponent} from "./components/answer/answers/answers.component";

const routes: Routes = [
  { path: '', component: AnswersComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
