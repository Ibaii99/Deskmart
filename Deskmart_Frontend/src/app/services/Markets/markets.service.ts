import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


const endpoint = "https://udbank-backend.herokuapp.com/api/v1/market/";

@Injectable({
  providedIn: 'root'
})
export class MarketsService {
  headers: HttpHeaders;

  constructor(private http: HttpClient) {
    this.headers = new HttpHeaders();
  }


  weekValue(company: string): Promise<any> {
    return this.http.get(`${endpoint}value/${company}`,{headers: this.headers}).toPromise();
  }
}
