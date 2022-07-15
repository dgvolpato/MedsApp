import { Component, OnInit } from '@angular/core';
import { MainService } from './services/main.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'frontend';
  daily_status:any;

  constructor(private service:MainService){}

  ngOnInit() {
    this.service.getStatus()
      .subscribe(response => {
        this.daily_status = response;
      })
  }

  take_pills() {
    console.log("clicked on take_pills()");
    this.service.putPillIntake();
    this.service.getStatus()
      .subscribe(response => {
        this.daily_status = response;
      })
  }
}
