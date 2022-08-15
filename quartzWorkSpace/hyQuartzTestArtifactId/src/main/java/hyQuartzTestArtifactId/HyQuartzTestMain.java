package hyQuartzTestArtifactId;

import org.quartz.JobBuilder;
import org.quartz.JobDetail;
import org.quartz.Scheduler;
import org.quartz.SchedulerException;
import org.quartz.SchedulerFactory;
import org.quartz.SimpleScheduleBuilder;
import org.quartz.SimpleTrigger;
import org.quartz.Trigger;
import org.quartz.TriggerBuilder;
import org.quartz.impl.StdSchedulerFactory;

public class HyQuartzTestMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello");
		
		SchedulerFactory schedulerFactory = new StdSchedulerFactory();
		
		try {
			Scheduler scheduler = schedulerFactory.getScheduler();
			scheduler = schedulerFactory.getScheduler();
			
			JobDetail job = JobBuilder.newJob(SimpleJob.class)
					  .withIdentity("myJob", "group1")
					  .usingJobData("jobSays", "Hello World!")
					  .usingJobData("myFloatValue", 3.141f)
					  .build();
			
			Trigger trigger = TriggerBuilder.newTrigger()
					  .withIdentity("myTrigger", "group1")
					  .startNow()
					  .withSchedule(SimpleScheduleBuilder.simpleSchedule()
					    .withIntervalInSeconds(10)
					    .repeatForever())
					  .build();
			
			scheduler.scheduleJob(job, trigger);
			
//			SimpleTrigger trigger = (SimpleTrigger) TriggerBuilder.newTrigger()
//					  .withIdentity("trigger2", "group1")
//					  .withSchedule(simpleSchedule()
//					    .withIntervalInSeconds(10)
//					    .withRepeatCount(10))
//					  .forJob("job1") 
//					  .build();
			
			scheduler.start();
		} catch (SchedulerException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
			

	}

}
