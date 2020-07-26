import {Answer} from "./answer";

export class Question {
  id:number;
  text:string;
  register:number;
  answers: Answer[];
}
