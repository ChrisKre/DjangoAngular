import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AnswersComponent } from './components/answer/answers/answers.component';
import { AnswerItemComponent } from './components/answer/answer-item/answer-item.component';
import { AddAnswerComponent } from './components/answer/add-answer/add-answer.component';
import {FormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    AnswersComponent,
    AnswerItemComponent,
    AddAnswerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
