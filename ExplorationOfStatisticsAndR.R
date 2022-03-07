# Simply exploration of Rstudio and R.
setA <- c(29, 36, 38, 32, 32, 33, 35, 32, 33, 30, 41, 22, 32, 30, 33, 42, 30, 41, 21, 28)
setB <- c(36, 30, 34, 29, 37, 42, 36, 14, 14, 44, 26, 17, 32, 34, 22, 26, 17, 11, 30, 34)

print("Question 3 part 1")
print(paste("Mean:",mean(setA))) 
print(paste("Median:",median(setA)))
print(paste("Sample Variance:",var(setA)))
print(paste("First Quantile:",quantile(setA,0.25)))
print(paste("Third Quantile:",quantile(setA,0.75)))
print(paste("Maximum:",max(setA)))
print(paste("Minimum:",min(setA)))

hist(setA)
boxplot(setA,setB,names=c("Set A","Set B"))

