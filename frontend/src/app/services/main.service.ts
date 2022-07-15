import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MainService {
  private status_url = 'http://localhost:8008/daily-status';
  private pill_intake_url = 'http://localhost:8008/pill-intake';

  intake:any;

  constructor(private httpClient: HttpClient) { }

  getStatus() {
    return this.httpClient.get(this.status_url)
  }

  putPillIntake() {
    const body = { message: 'put pill intake'}
    return this.httpClient.put<any>(this.pill_intake_url, body)
      .subscribe(data => this.intake = data.intake)
  }

}
