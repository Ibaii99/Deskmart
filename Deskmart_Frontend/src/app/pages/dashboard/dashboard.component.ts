
import { Component, OnDestroy } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { BackendService } from 'app/services/deskmart-backend/backend.service';
import { ToastrService } from 'ngx-toastr';
import { NotificationsService } from 'app/services/Notification/notifications.service';

import { interval, Subscription } from 'rxjs';
import * as moment from 'moment';


const sensorInterval = interval(120000);
const weatherInterval = interval(120000);


@Component({
  selector: "dashboard-cmp",
  moduleId: module.id,
  templateUrl: "dashboard.component.html",
})
export class DashboardComponent implements OnDestroy {
  
  public canvas: any;
  public ctx;
  public chartColor;
  
  sensorSubscription: Subscription = sensorInterval.subscribe(val => this.loadSensors());
  weatherSubscription: Subscription = weatherInterval.subscribe(val => this.loadWeather());
  private today = new Date();
  private dd = String(this.today.getDate()).padStart(2, '0');
  private mm = String(this.today.getMonth() + 1).padStart(2, '0'); //January is 0!
  private yyyy = String(this.today.getFullYear());

  public areaChart;
  private pieChart;
  private linealChart;
  private lineChart;



  visible: boolean = true;
  selectable: boolean = true;
  removable: boolean = true;
  addOnBlur: boolean = false;
  dates: [];

  color_capacitor11: string = "#FFFFFF";
  color_capacitor12: string = "#FFFFFF";
  color_capacitor21: string = "#FFFFFF";
  color_capacitor22: string = "#FFFFFF";

  formGroup: FormGroup;

  noti: NotificationsService;

  now: String= moment(new Date(), 'H:mm:ss').format("H:mm:ss");

  constructor(private fb: FormBuilder, private backend: BackendService, private toastr: ToastrService){
    this.noti = new NotificationsService(this.toastr);

    this.formGroup = fb.group({
      weatherTemperature: new FormControl(''),
      weatherDescription: new FormControl(''),
      weatherHumidity: new FormControl(''),
      insideTemperature: new FormControl(''),
      insideHumidity: new FormControl(''),
      temperatureAlert: new FormControl(''),
      color_capacitor11: new FormControl('#FFFFFF'),
      color_capacitor12: new FormControl('#FFFFFF'),
      color_capacitor21: new FormControl('#FFFFFF'),
      color_capacitor22: new FormControl('#FFFFFF'),

      time_capacitor11: new FormControl('0:0:0s'),
      time_capacitor12: new FormControl('0:0:0s'),
      time_capacitor21: new FormControl('0:0:0s'),
      time_capacitor22: new FormControl('0:0:0s'),

      dateSelected: new FormControl(this.dd+'/'+this.mm+'/'+this.yyyy),
      capacitorTouches: new FormControl(0),

    });
    this.loadWeather();
    this.loadSensors();
    this.get_different_days();
    
  }


  loadWeather(){
    this.backend.get_weather().then(
      (weather) => {
        this.formGroup.controls.weatherTemperature.setValue(weather.temperatura);
        this.formGroup.controls.weatherDescription.setValue(weather.tiempo);
        this.formGroup.controls.weatherHumidity.setValue(weather.humedad);
      }
    );
  }

  loadSensors(){
    this.get_flame();
    this.loadCapacitors();
    this.get_humidity();
    this.get_temperature();
  }

  get_humidity(){
    this.backend.get_last_humidity().then(
      (humidity) => {
        this.formGroup.controls.insideHumidity.setValue(humidity[2]);
      }
    );
  }

  get_temperature(){
    this.backend.get_last_temperature().then(
      (temperature) => {
        this.formGroup.controls.insideTemperature.setValue(temperature[2]);
      }
    );
  }

  get_flame(){
    this.backend.get_last_flame().then(
      (alert) => {
        this.formGroup.controls.temperatureAlert.setValue(alert[2]);
        if(alert[2]==1){
          this.noti.showNotification('top', 'center', "error", "Temperature alert", "Your temperature exceeds 38°C");
        }
      }
    );
  }

  loadCapacitors(){
    this.get_heat_map();
    this.get_individual_touches();
    this.get_total_touches();
  }

  get_heat_map(){
    this.backend.get_heat_map(this.dd, this.mm, this.yyyy).then(
      (capacitors) => {
        this.formGroup.controls.color_capacitor11.setValue(capacitors.cap11);
        this.formGroup.controls.color_capacitor12.setValue(capacitors.cap12);
        this.formGroup.controls.color_capacitor21.setValue(capacitors.cap21);
        this.formGroup.controls.color_capacitor22.setValue(capacitors.cap22);

      }
    );
  }

  get_different_days(){
    this.backend.get_different_days().then(
      (days) => {
        console.log(days);
        this.dates = days;
      });
  }

  get_total_touches(){
    this.backend.get_touch_times(this.dd, this.mm, this.yyyy).then(
      (touches) => {
        var seconds = touches * 3.54 ;
        var hours = Math.floor(seconds / 3600);
        var minutes = Math.floor(seconds / 60);
        seconds = Math.round(seconds % 60);
        var time = hours + ':' + minutes + ':' + seconds + 's';
        this.formGroup.controls.capacitorTouches.setValue(time);
      }
    );
  }

  get_individual_touches(){

    this.backend.get_touch_map(this.dd, this.mm, this.yyyy).then(
      (caps) => {

        var seconds_cap11 = caps.cap11 * 3.54 ;
        var hours_cap11 = Math.floor(seconds_cap11 / 3600);
        var minutes_cap11 = Math.floor(seconds_cap11 / 60);
        seconds_cap11 = Math.round(seconds_cap11 % 60);
        var time_cap11 = hours_cap11 + ':' + minutes_cap11 + ':' + seconds_cap11 + 's';
        

        var seconds_cap12 = caps.cap12 * 3.54 ;
        var hours_cap12 = Math.floor(seconds_cap12 / 3600);
        var minutes_cap12 = Math.floor(seconds_cap12 / 60);
        seconds_cap12 = Math.round(seconds_cap12 % 60);
        var time_cap12 = hours_cap12 + ':' + minutes_cap12 + ':' + seconds_cap12 + 's';
        
        var seconds_cap21 = caps.cap21 * 3.54 ;
        var hours_cap21 = Math.floor(seconds_cap21 / 3600);
        var minutes_cap21 = Math.floor(seconds_cap21 / 60);
        seconds_cap21 = Math.round(seconds_cap21 % 60);
        var time_cap21 = hours_cap21 + ':' + minutes_cap21 + ':' + seconds_cap21 + 's';
        
        var seconds_cap22 = caps.cap22 * 3.54 ;
        var hours_cap22 = Math.floor(seconds_cap22 / 3600);
        var minutes_cap22 = Math.floor(seconds_cap22 / 60);
        seconds_cap22 = Math.round(seconds_cap22 % 60);
        var time_cap22 = hours_cap22 + ':' + minutes_cap22 + ':' + seconds_cap22 + 's';
        
        this.formGroup.controls.time_capacitor11.setValue(time_cap11);
        this.formGroup.controls.time_capacitor12.setValue(time_cap12);
        this.formGroup.controls.time_capacitor21.setValue(time_cap21);
        this.formGroup.controls.time_capacitor22.setValue(time_cap22);
        

        // var seconds = touches * 3.54 ;
        // var hours = Math.floor(seconds / 3600);
        // var minutes = Math.floor(seconds / 60);
        // seconds = Math.round(seconds % 60);
        // var time = hours + ':' + minutes + ':' + seconds + 's';
        // this.formGroup.controls.capacitorTouches.setValue(time);
      }
    );
    
  }

  reload(){
    this.now = moment(new Date(), 'H:mm:ss').format("H:mm:ss");
    this.loadSensors();
    this.loadWeather();
  }
  ngOnDestroy() {
    this.sensorSubscription.unsubscribe();
    this.weatherSubscription.unsubscribe();
  }

  selectDate(date){
    this.dd = date.split("/")[0];
    this.mm = date.split("/")[1];
    this.yyyy = date.split("/")[2];
    this.formGroup.controls['dateSelected'].setValue(this.dd+'/'+this.mm+'/'+this.yyyy);
    this.loadCapacitors();
  }
}
