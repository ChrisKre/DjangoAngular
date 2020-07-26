import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AnswersComponent } from './components/answer/answers/answers.component';
import { AnswerItemComponent } from './components/answer/answer-item/answer-item.component';
import { AddAnswerComponent } from './components/answer/add-answer/add-answer.component';
import {FormsModule} from "@angular/forms";

import { CovalentLayoutModule } from '@covalent/core/layout';
import { CovalentStepsModule  } from '@covalent/core/steps';
/* any other core modules */
// (optional) Additional Covalent Modules imports
import { CovalentHttpModule } from '@covalent/http';
import { CovalentHighlightModule } from '@covalent/highlight';
import { CovalentMarkdownModule } from '@covalent/markdown';
import { CovalentDynamicFormsModule } from '@covalent/dynamic-forms';
import { CovalentBaseEchartsModule } from '@covalent/echarts/base';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatListModule} from "@angular/material/list";
import {MatIconModule} from "@angular/material/icon";
import { RegistersComponent } from './components/register/registers/registers.component';
import { RegisterItemComponent } from './components/register/register-item/register-item.component';
import { AddRegisterComponent } from './components/register/add-register/add-register.component';
import { SidenavComponent } from './components/layout/sidenav/sidenav.component';

@NgModule({
  declarations: [
    AppComponent,
    AnswersComponent,
    AnswerItemComponent,
    AddAnswerComponent,
    RegistersComponent,
    RegisterItemComponent,
    AddRegisterComponent,
    SidenavComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    CovalentLayoutModule,
    CovalentStepsModule,
    // (optional) Additional Covalent Modules imports
    CovalentHttpModule.forRoot(),
    CovalentHighlightModule,
    CovalentMarkdownModule,
    CovalentDynamicFormsModule,
    CovalentBaseEchartsModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatListModule,
    MatIconModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
