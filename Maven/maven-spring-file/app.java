/* 
* The Java code from the project shows how Spring Boot can be used.
*/

@RestController 
@SpringBootApplication
public class ControllerAndMain {

@RequestMapping("/") public String hello() {
return "hello\n"; 
}

public static void main(String[] args) { 
    SpringApplication.run(ControllerAndMain.class, args);
} 

}