import {Question} from "./question";

export enum RegisterType {
  LANGUAGE = 'LAN',
  SOFTWARE = 'SFW',
  KNOWLEDGE = 'KLG',
}

export class Register{
  id:number;
  owner:number;
  name: string;
  type: RegisterType;
  questions: Question[];
}

